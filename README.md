# Implementation of Wynn's Epsilon Method For Convergence Acceleration
For most convergent series, the rate of convergence can be accelerated by applying Shank's Transformation, which approximates the limit of a sequence in a non-linear fashion. That is, for a series of the form:

<p align="center">
  <img width="150" height="75" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ec37238b37bf8eacbdd244beeb8e6da607b17021">
</p>

Shank's Transformation is defined as:

<p align="center">
  <img width="300" height="200" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/54465b7c5c77f1cc947595def797ac7a62064a74">
</p>

Where A<sub>p</sub> are the pth partial sums of the sequence, and ΔA<sub>p</sub> = A<sub>p+1</sub> - A<sub>p</sub>.
This gives a method to solve for the k<sup>th</sup>-order Shank's Transformation. Peter Wynn introduced an efficient algorithm for computing the k<sup>th</sup> Shank's Transformation of a partial sum and is given by the following:


<p align="center">
  <img width="400" height="75" src="http://www.adamponting.com/wp-content/ql-cache/quicklatex.com-91b574374d16e4cc835dc61a880325a8_l3.png">
</p>

<p align="center">
  <img width="150" height="100" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa16105f38678c4b8151cd1ac1cd1a0a8d219c6">
</p>
