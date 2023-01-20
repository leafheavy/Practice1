#Machine Learning

##Supervised Learning：
there are right answers in the data sets which people give to
porpuse:produce more right answers
**data set<=>training set**

##Unsupervised Learning
there are **not** right answers in the date sets which people give to
porpuse:find structure in the data

##Regression
predicting a real-valued output
##Classfication
predicting discrete-valued outputs

##Liner regression
* **hypothesis function:**$h(x) = \theta_{0} + \theta_{1}x$
* **training set:**$(x^i,y^i)$
* **cost function:**$J(\theta_{0},\theta_{1})\frac{1}{2m}\sum_{i=1}^{m}[h(x^i)-y^i]^2$
###goal
finding certificated $(x^i,y^i)$ to make the calue of cost function minimized
![cost function](https://img-blog.csdnimg.cn/img_convert/252cf47845b1c64efb8774bdde058f62.png)

###Gradient Decent
* initialize $\theta_{0},\theta_{1}$
* keep changing $\theta_{0},\theta_{1}$ to reduce the value of $J(\theta_{0},\theta_{1})$
* $$\theta_{j}=\theta_{j}-\alpha\frac{\partial}{\partial\theta_{j}}J(\theta_{0},\theta_{1})$$(simultaneously updata j=0 and j=1)
* $\alpha$:learning rate
* **$\alpha\frac{\partial}{\partial\theta_{j}}J(\theta_{0},\theta_{1})$**:learning step **will update automatically**



