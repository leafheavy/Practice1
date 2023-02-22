# Machine Learning

## Supervised Learning：
there are right answers in the data sets which people give to
porpuse:produce more right answers
**data set<=>training set**

## Unsupervised Learning
there are **not** right answers in the date sets which people give to
**porpuse:** find structure in the data

## Regression
predicting a real-valued output
##Classfication
predicting discrete-valued outputs

## Liner regression
* **hypothesis function:**$f(x) = b + w_{1}x$
* **training set:**$(x^i,y^i)$
* **cost function:**$J(b,w_{1}) = \frac{1}{2m}\sum_{i=1}^{m}[h(x^i)-y^i]^2$

## Multivariate linear regrassion
* **hypothesis function:**
$$ f(x) = b + w_{1}x_{1} + \theta_{2}x_{2} +... + w_{n}x_{n} = w^{T}x $$
* **define data:**
$ m: $ the nunmber of the collected samples
$ n: $ the number of features
$ x^i: $ the $i^{th}$ training sample
$ x^i_j: $ value of the $j^{th}$ feature in the $x^i$
$$x = \left[\begin{matrix}x_{1}\\\vdots\\x_{n}\\\end{matrix}\right]w = \left[\begin{matrix}w_{1}\\\vdots\\w_{n}\\\end{matrix}\right]$$
* **training set:**
$(x^i,y^i)$
* **cost function:**
$J(b,w_{1},...,w_{n}) =  J(b, w) = \frac{1}{2m}\sum_{i=1}^{m}[h(x^i)-y^i]^2$
![1](https://img-blog.csdnimg.cn/img_convert/252cf47845b1c64efb8774bdde058f62.png)

## Polynomial regression
* **hypothesis function:**
$$ f(x) = b + w_{1}x_{1} + \theta_{2}x^2 +... + w_{n}x^n $$

### Logicstic Regression
* **sigmoid function:**$$ g(z) = \frac{1}{1+e^{-z}}$$
* **hypothesis function:**$$f(b, w) = z = w x + b$$
    * ***Also we can use polynomial regression to replace this one***
* **Output of logicstic regression:**$$f(b, w) = \frac{1}{1+e^{-(w x + b)}}$$
![1](https://img-blog.csdnimg.cn/img_convert/2c3cac4f95e4d5fec22b3e2ba72ca1c8.png)
* **Decision boundary**$$ z = 0 $$
* **cost function:**
$$ J(b, w) = \frac{1}{2}\sum_{i=1}^{m} L(h(x^{i}), y^{i})$$
    * **Loss function:**
    ![1](https://img-blog.csdnimg.cn/img_convert/fcc90fe0621ff637842d0e2fa03a7fd5.png)

## Goal
finding certificated $(b, w)$ to make the calue of cost function $J(b, w)$ **minimized**(in other words:**"just right"**)
![1](https://img-blog.csdnimg.cn/img_convert/55f6cf26ded5b993b0c33d5d3d1a0ca5.png)
* Collect more traning examples
* Feature collection
* Regularization-Reduce size of parameters **which aren't necessary than others**
    * **Regularization cost function:**$$J(b, w) + \mu\ L_2$$

    $L_{2}:\sum_{j = 1}^{n} w_{j}^{2} < 1$
    $L_{1}:\sum_{j = 1}^{n} |w_{j}^{2}|$

    * **Lasso Regression:**
    $$ Loss = J(b, w) + \mu L_{1} $$ ***It can sparsification parameters***
        * **Restrictions:**$$(|w_{1}| + |w_{2}|) <= 1$$
        ![1](https://img-blog.csdnimg.cn/img_convert/f80e3ad613c892a5385e70b8d19431df.png)
        ![1](https://img-blog.csdnimg.cn/img_convert/e405cd23dfb48e19e1dc85ecccb1df1c.png)
    * **Ridge regression:**
    $$ Loss = J(b, w) + \mu L_{2} $$
        * **Restrictions:**$$(w_{1}^{2} + w_{2}^{2}) <= 1$$
        ![1](https://img-blog.csdnimg.cn/img_convert/24db9d1eb0eff21afb3f9d0ad21361ae.png)

### Gradient Decent
* initialize $b,w_{1},...,w_{n}$
* keep changing $b,w_{1}...,w_{n}$ to reduce the value of $J(w)$
$$w_{j}=w_{j}-\alpha\frac{\partial}{w_{j}}J(b,w)$$(simultaneously updata j=0,1,...,n)
    * **In Regularization Or in Polynomial regression:**$$w_{j}=w_{j}-\alpha(\frac{\partial}{w_{j}}J(b,w) + \mu w_{j})$$(simultaneously updata j=0,1,...,n)
* **$\alpha\frac{\partial}{w_{j}}J(b,w_{1})$**:learning step **will update automatically**

## Data Operation
* **Feature Scaling**
    * idea:Make sure features are on a similar scale(Usually get every feature into approximately a $-1<=x_i<=1$ range)

* **Mean normalization**
    * Replace $x_i$ with $x_i-\mu_{i}$ to make features has approximately zero mean

* **$\alpha$:learning rate**
    ![1](https://img-blog.csdnimg.cn/img_convert/1021cee4dbb7f1d75298fa06beaa2e44.png)
    ![1](https://img-blog.csdnimg.cn/img_convert/b81c1b9774ddcdc97c08aef701dd5245.png)


## Nutural Networks
* Constuction:
    **Input Layer**->**Hidden Layers**->**Output Layer**
    each layer = one vecter
    **computer will find the hidden layer by itself**
    superscripts square $[i]$ express the $i_{th}$ hidden layer
* Each neuron also called unit
* The value of each neuron's activation form vecter $\vec{a}$
    Each neuron has input vecter and output vecter
    $\vec{a}^{[i]}_{j}=g(w^{[i]}_{j}\vec{a}^{[i-1]}+b^{[i]}_{j})$
    **Activation function g express a logical relationship**

## Forward propagation
* neurons in layer will decline from $0_{th}$ layer to ending layer
* calculate from $0_{th}$ layer to ending layer








