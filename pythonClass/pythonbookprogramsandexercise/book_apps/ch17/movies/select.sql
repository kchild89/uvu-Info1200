SELECT movieID, Movie.name, year, minutes,
	Movie.categoryID AS categoryID, 
	Category.name AS categoryName
FROM Movie 
    JOIN Category ON Category.categoryID = Movie.categoryID
WHERE Movie.categoryID = 1
