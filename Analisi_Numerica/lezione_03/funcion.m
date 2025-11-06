function [x, r, iter, errvec] = newton(Ffun, Jfun, x0, tol, nmax, p)
	% x è la soluzione con n componenti
	% r è la norma del residuo (norma euclidea) (il residuo è F(X)K??)
	iter = 0; err = tol + 1; x = x0;
	errvec = [];
	Jx = Jfun(x); 
	[L,U,P] = lu(Jx);
	step = 0;
	while err > tol && iter < nmax
		if step == p
			step = 0;
			Jx = Jfun(x);
			[L,U,P] = lu(Jx);
		end
		Fx = Ffun(x);
		Fx = P * Fx;
		y = forwardrow(L, Fx);
		deltax = - backwardrow(U,y);
		x = x + deltax;
		err = norm(deltax);
		errvec = [errvec; err];
		iter += 1;
		step += 1;
	end
	r = norm(Ffun(x));
end
