function F = Ffun(x)
	F = zeros(2,1);
	F(1) = exp(x(1))^2 + x(2)^2) - 2;
	F(2) = exp(x(1)^2 - x(2)^2) - 1;
end
