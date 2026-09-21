"""Run with python3 september/calculator.py to open the calculator."""

import ast
import json
import math
import operator
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def calculate(expression):
    """Evaluate arithmetic only, without executing Python code."""
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Enter a calculation first.")
    if len(expression) > 200:
        raise ValueError("Calculation is too long.")
    operations = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](evaluate(node.left), evaluate(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        raise ValueError("Use numbers, parentheses, and + − × ÷ only.")

    try:
        result = evaluate(ast.parse(expression.strip(), mode="eval").body)
        if not math.isfinite(result):
            raise ValueError("Result is too large.")
        return format(result, ".12g")
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.") from None
    except (SyntaxError, TypeError):
        raise ValueError("Check your calculation.") from None
    except (OverflowError, RecursionError):
        raise ValueError("Calculation is too large.") from None


PAGE = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Calculator</title>
<style>
* { box-sizing: border-box; }
body { margin: 0; min-height: 100vh; display: grid; place-items: center;
  background: #101827; color: #f3f6fb; font-family: system-ui, sans-serif; padding: 20px; }
main { width: min(100%, 380px); padding: 26px; border: 1px solid #354257;
  background: #1b2739; border-radius: 24px; box-shadow: 0 24px 70px #0005; }
h1 { font-size: 20px; margin: 0 0 22px; font-weight: 600; }
label { display: block; color: #b5c4d9; font-size: 13px; margin-bottom: 8px; }
input { width: 100%; padding: 18px 12px; border: 1px solid #455671;
  border-radius: 12px; background: #101827; color: white; text-align: right;
  font-size: 30px; outline-offset: 3px; }
#status { min-height: 42px; padding: 8px 0; font-size: 13px; color: #b5c4d9; overflow-wrap: anywhere; }
.keys { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
button { min-height: 58px; border: 0; border-radius: 12px; background: #30415b;
  color: white; font: 500 22px system-ui; cursor: pointer; }
button:hover { filter: brightness(1.2); }
button:active { transform: scale(.96); }
button:focus-visible { outline: 3px solid #8ebeff; outline-offset: 2px; }
.operator { background: #284f77; color: #c5e3ff; }
.clear { color: #ffbdba; }
.equals { background: #80c5ff; color: #102438; }
footer { margin-top: 20px; text-align: center; color: #b5c4d9; font-size: 12px; }
</style>
<main>
  <h1>Calculator</h1>
  <label for="expression">Your calculation</label>
  <input id="expression" type="text" inputmode="decimal" placeholder="0"
    autocomplete="off" spellcheck="false" maxlength="200" autofocus>
  <div id="status" role="status" aria-live="polite">Ready when you are.</div>
  <div class="keys">
    <button class="clear" data-action="clear" aria-label="Clear">AC</button>
    <button data-value="(">(</button><button data-value=")">)</button>
    <button class="operator" data-value="/" aria-label="Divide">÷</button>
    <button data-value="7">7</button><button data-value="8">8</button><button data-value="9">9</button>
    <button class="operator" data-value="*" aria-label="Multiply">×</button>
    <button data-value="4">4</button><button data-value="5">5</button><button data-value="6">6</button>
    <button class="operator" data-value="-" aria-label="Subtract">−</button>
    <button data-value="1">1</button><button data-value="2">2</button><button data-value="3">3</button>
    <button class="operator" data-value="+" aria-label="Add">+</button>
    <button data-value="0">0</button><button data-value=".">.</button>
    <button data-action="delete" aria-label="Delete last character">⌫</button>
    <button class="equals" data-action="equals" aria-label="Equals">=</button>
  </div>
  <footer>Enter to calculate · Escape to clear</footer>
</main>
<script>
const field = document.querySelector('#expression');
const status = document.querySelector('#status');
function clear() { field.value = ''; status.textContent = 'Ready when you are.'; field.focus(); }
async function solve() {
  const expression = field.value;
  try {
    const response = await fetch('/calculate', {method: 'POST',
      headers: {'Content-Type': 'application/json'}, body: JSON.stringify({expression})});
    const data = await response.json();
    if (field.value !== expression) return;
    if (!response.ok) { status.textContent = data.error; return; }
    field.value = data.result;
    status.textContent = expression + ' = ' + data.result;
  } catch { status.textContent = 'Connection lost. Restart calculator.py to reconnect.'; }
  field.focus();
}
document.querySelector('.keys').addEventListener('click', event => {
  const button = event.target.closest('button');
  if (!button) return;
  const action = button.dataset.action;
  if (action === 'clear') return clear();
  if (action === 'equals') return solve();
  let start = field.selectionStart, end = field.selectionEnd;
  if (action === 'delete' && start === end) start = Math.max(0, start - 1);
  const value = button.dataset.value || '';
  if (field.value.length - (end - start) + value.length > 200) return;
  field.setRangeText(value, start, end, 'end');
  status.textContent = ''; field.focus();
});
field.addEventListener('keydown', event => {
  if (event.key === 'Enter' || event.key === '=') { event.preventDefault(); solve(); }
  if (event.key === 'Escape') { event.preventDefault(); clear(); }
});
</script>
</html>"""


class CalculatorHandler(BaseHTTPRequestHandler):
    def respond(self, code, content, content_type):
        body = content.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return
        self.respond(200, PAGE, "text/html; charset=utf-8")

    def do_POST(self):
        if self.path != "/calculate":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 4096:
                raise ValueError("Invalid request size.")
            payload = json.loads(self.rfile.read(length))
            if not isinstance(payload, dict):
                raise ValueError("Invalid request.")
            result = calculate(payload.get("expression", ""))
            self.respond(200, json.dumps({"result": result}), "application/json")
        except (ValueError, UnicodeDecodeError) as error:
            self.respond(400, json.dumps({"error": str(error)}), "application/json")

    def log_message(self, format, *args):
        pass


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), CalculatorHandler)
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"Calculator running at {url}\nPress Ctrl+C to stop.", flush=True)
    threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nCalculator closed.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
