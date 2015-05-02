function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%


temp = ones([5000, 1]);
temp1 = [temp, X];


%temp2 = temp1*Theta1';
%g2 = sigmoid(temp2);

save('temp.mat', 'temp', 'temp1', 'g2');
%m2 = size(g2, 1);
%temp3 = ones([5000, 1]);
%temp4 = [temp3, g2];
%temp5 = temp4*Theta2';
%p2 = sigmoid(temp5);











% =========================================================================


end
