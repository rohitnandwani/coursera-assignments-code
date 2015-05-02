X1 = [ones(20,1) (exp(1) + exp(2) * (0.1:0.1:2))'];
Y1 = X1(:,2) + sin(X1(:,1)) + cos(X1(:,2));
X2 = [X1 X1(:,2).^0.5 X1(:,2).^0.25];
Y2 = Y1.^0.5 + Y1;

[theta, J_history, delta] = gradientDescent(X1, Y1, [0.5 -0.5]', 0.01, 10);