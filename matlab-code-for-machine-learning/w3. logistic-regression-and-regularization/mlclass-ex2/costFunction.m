function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%

step0 = X*theta;
step1 = sigmoid(step0);
step2 = log(step1);
step3 = -1 * y;
step4 = step3' * step2;


%step5 = X*theta;
%step6 = sigmoid(step5);
step7 = 1 - step1;
step8 = log(step7);
step9 = 1 - y;
step10 = step9' * step8;

J = (step4 - step10)/m;

step11 = step1 - y;
step12 = step11' * X;
grad = (step12)/m;




% =============================================================

end
