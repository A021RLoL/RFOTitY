# 代码生成时间: 2025-10-02 01:48:33
import numpy as np
from scipy.special import expit as sigmoid

# 激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 损失函数
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

# 梯度下降优化器
class GradientDescentOptimizer:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def optimize(self, weights, gradients):
        return weights - self.learning_rate * gradients

# 神经网络
class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        # 设置节点数
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # 初始化权重矩阵和偏置向量
        self.weights_input_to_hidden = np.random.rand(self.input_nodes, self.hidden_nodes)
        self.weights_hidden_to_output = np.random.rand(self.hidden_nodes, self.output_nodes)
        self.bias_hidden = np.random.rand(self.hidden_nodes)
        self.bias_output = np.random.rand(self.output_nodes)

    def feedforward(self, X):
        # 前向传播
        self.hidden_layer_input = np.dot(X, self.weights_input_to_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_to_output) + self.bias_output
        self.output_layer_output = sigmoid(self.output_layer_input)
        return self.output_layer_output

    def backpropagation(self, X, y, y_pred):
        # 反向传播
        output_error = y - y_pred
        output_delta = output_error * sigmoid_derivative(y_pred)
        hidden_error = output_delta.dot(self.weights_hidden_to_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer_output)

        # 梯度
        output_gradient = output_delta.dot(self.hidden_layer_output.T)
        hidden_gradient = hidden_delta.dot(X.T)

        return {
            'output_gradient': output_gradient,
            'hidden_gradient': hidden_gradient,
            'output_weights_gradient': self.hidden_layer_output.T,
            'hidden_weights_gradient': X.T,
        }

    def train(self, X, y, epochs, optimizer):
        for epoch in range(epochs):
            for X_batch, y_batch in zip(X, y):
                # 前向传播
                y_pred = self.feedforward(X_batch.reshape(1, -1))
                
                # 反向传播
                gradients = self.backpropagation(X_batch.reshape(1, -1), y_batch, y_pred)

                # 更新权重和偏置
                self.weights_input_to_hidden -= optimizer.optimize(
                    self.weights_input_to_hidden,
                    gradients['hidden_weights_gradient'].dot(gradients['hidden_gradient'])
                )

                self.weights_hidden_to_output -= optimizer.optimize(
                    self.weights_hidden_to_output,
                    gradients['output_weights_gradient'].dot(gradients['output_gradient'])
                )

                self.bias_hidden -= optimizer.optimize(self.bias_hidden, gradients['hidden_gradient'])
                self.bias_output -= optimizer.optimize(self.bias_output, gradients['output_gradient'])

            # 打印损失
            if (epoch + 1) % 100 == 0:
                loss = mse_loss(y, self.feedforward(X))
                print(f'Epoch {epoch + 1}, Loss: {loss:.4f}')

# 示例数据
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

# 创建神经网络
nn = NeuralNetwork(2, 4, 1)

# 创建优化器
optimizer = GradientDescentOptimizer(learning_rate=0.1)

# 训练神经网络
nn.train(X_train, y_train, epochs=1000, optimizer=optimizer)