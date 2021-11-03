

compute gcd of 2 numbers
[
	decla int a;
	decla int b;
	decla int i;
	decla int gcd;
	
	read(a);
	read(b);
	
	i = 0;
	gcd = 0;
	
	for i in i<=a and i<=b with i = i + 1 do
		if i%a==0 and i%b==0 do
			gcd = i;
	
	show(gcd);
]