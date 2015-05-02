function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

predictions = X*theta;
sqErrors = (predictions-y).^2;
J = 1/(2*m) * sum(sqErrors);

step1 = theta(2:end)' * theta(2:end);
step3 = lambda/(2*m);
step4 = step3 * step1;
J = J + step4;

delta = (X*theta - y)';
delta = delta * X;
grad = delta' / m;


step5 =(lambda/m)*theta(2:end);
save('temp.mat', 'grad', 'step5')
grad(2:end) = grad(2:end) + step5;




% =========================================================================

grad = grad(:);

end
