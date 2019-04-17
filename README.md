# Implementation of Wynn's Epsilon Method For Convergence Acceleration
For most convergent series, the rate of convergence can be accelerated by applying the [Shanks Transformation](https://en.wikipedia.org/wiki/Shanks_transformation), which approximates the limit of a sequence in a non-linear fashion. That is, for a series of the form:

<p align="center">
  <img width="150" height="75" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ec37238b37bf8eacbdd244beeb8e6da607b17021">
</p>

The Shanks Transformation is defined as:

<p align="center">
  <img width="300" height="200" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/54465b7c5c77f1cc947595def797ac7a62064a74">
</p>

Where A<sub>p</sub> are the pth partial sums of the sequence, and ΔA<sub>p</sub> = A<sub>p+1</sub> - A<sub>p</sub>.
This gives a method to solve for the k<sup>th</sup>-order Shank's Transformation. Peter Wynn introduced an efficient algorithm for computing the k<sup>th</sup> Shanks Transformation of a partial sum and is given by the following:


<p align="center">
  <img width="400" height="50" src="http://www.adamponting.com/wp-content/ql-cache/quicklatex.com-91b574374d16e4cc835dc61a880325a8_l3.png">
</p>
Here, each ε<sub>2k</sub> is the equivalent of applying the k<sup>th</sup> Shanks Transformation to the n<sup>th</sup> partial sum S<sub>n</sub>. ε<sub>0</sub> is defined as S<sub>n</sub>, and the primary diagonal gives the next approximation.
For this example, take the Gregory-Leibniz series for calculating π:
<p align="center">
  <img width="150" height="100" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa16105f38678c4b8151cd1ac1cd1a0a8d219c6">
</p>
This series will eventually converge to π, but it will take thousands of terms to get even a decent a approximation! Just take a look at http://www.eveandersson.com/pi/gregory-leibniz. Even after 1000 terms, the series is only accurate to 2 decimal places.<br/>
<br/>

wynnpi.py takes an integer arguement N and implements Wynn's epsilon method to find a highly precise approximation for π after N terms of the Gregory-Leibniz series.
