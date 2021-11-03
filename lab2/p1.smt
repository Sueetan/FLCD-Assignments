compute de max of 3 numbers
[
	decla int a ;
	decla int b ;
	decla int c ;
	decla int max ;
	decla string d ;

	d = "something" ;
	
	read ( a ) ;
	read ( b ) ;
	read ( c ) ;
	
	if a > b do
		max = a ;
	else if b > a and b > c do
		max = b ;
	else do
		max = c ;
		
	write ( max ) ;
]
