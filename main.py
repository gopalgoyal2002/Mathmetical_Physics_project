import copy # for deepcopy function
import numpy as np
from sympy import Matrix
from numpy.linalg import eig
import scipy.linalg as la

class Matrix1(object):
	'''This is the main class for all 2x2 and 3x3 matrices.
	It contains all functions that can be used commonly for both the types of matrices that we deal with in this project.
	It serves as the parent class for the classes: twoBytwo and threeBythree.
	'''

	def __init__(self,A,order):
		self.A = copy.deepcopy(A)
		self.order = order


	def __str__(self): # overides the str function and prints the numbers in the form of a matrix (in our case, it returns HTML to facilitate printing on the webpage)
		returned_string = "<table>"

		for i in range(1,self.order+1):
			returned_string += "<tr>"
			for j in range(1,self.order+1):
				returned_string += "<td>" + str(self.A[i][j]) + "</td>"
			returned_string += "</tr>"

		returned_string += '</table>'

		return returned_string


	def transpose(self): # returns the transpose of 2x2 and 3x3 matrix depending on the order of the Matrix object
		inverted = copy.deepcopy(self.A)
		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				inverted[j][i] = self.A[i][j]

		return Matrix1(inverted,self.order)


	def multiply(self,other): # returns the multiplication of two square matrices of the same order
		multi = copy.deepcopy(self.A)

		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				for k in range(1,self.order+1):
					multi[i][j] += self.A[i][k] * other.A[k][j]
				multi[i][j] = multi[i][j]-self.A[i][j]
		return Matrix1(multi,self.order)


class twoBytwo(Matrix1):
	''' This is a sub-class of the Matrix class and is specific to 2x2 matrices.
	We use the OOP concept of inheritance to inherit the initialization, str, transpose and multiply functions from the main class.
	This class mainly defines the determinant and inverse functions for 2x2 matrices.
	'''

	def determinant(self): # returns the determinant of the 2x2 matrix represented by the current object
		B = self.A
		ans = (B[1][1] * B[2][2]) - (B[2][1] * B[1][2])
		return ans

	def inverse(self): # returns the inverse of a 2x2 object if it exists, or informs the user in case the determinant does not exist
		det = self.determinant()

		if det == 0:
			return "Inverse does not exist."
		adj = copy.deepcopy(self.A)
		m=[[adj[1][1],adj[1][2]],[adj[2][1],adj[2][2]]]
		m1=Matrix(m)
		r=1
		c=1
		x,y=m1.jordan_form()
		# print(y)
		for i in y:
			print(i)
			if(r==1):
			    adj[1][1]=i
			if(r==2):
				adj[1][2]=i
			if(r==3):
				adj[2][1]=i
			if(r==4):
				adj[2][2]=i
			r+=1
			

		
		return Matrix1(adj,2)


class threeBythree(Matrix1):
	''' This is a sub-class of the Matrix class and is specific to 3x3 matrices.
	We use the OOP concept of inheritance to inherit the initialization, str, transpose and multiply functions from the main class.
	This class mainly defines the determinant and inverse functions for 3x3 matrices.
	'''

	def determinant(self): # returns the determinant of the 3x3 matrix represented by the current object
		B = self.A
		ans = 0
		for x in range(1,self.order+1):
			z = []

			for i in range(2,self.order+1):
				for j in range(1,self.order+1):
					if j==x:
						pass
					else:
						z.append(B[i][j])

			Z = [None,[None,z[0], z[1]], [None,z[2], z[3]]]
			twoBytwoSub = twoBytwo(copy.deepcopy(Z),2)
			subDeterminant = twoBytwoSub.determinant()
			if x%2==0:
				ans += -B[1][x] * subDeterminant
			else:
				ans += B[1][x] * subDeterminant
		return ans


	def inverse(self): # returns the inverse of a 3x3 object if it exists, or informs the user in case the determinant does not exist
		B = self.A
		cofactors = copy.deepcopy(self.A)
		coFactorElem = 0

		mainDeterminant = self.determinant()

		if mainDeterminant == 0:
			return "Inverse does not exist."

        
		adj = copy.deepcopy(self.A)
		# print(B)
		# m=[[adj[1][1],adj[1][2],adj[1][3]],
		#     [adj[2][1],adj[2][2],adj[2][3]],
		# 	[adj[3][1],adj[3][2],adj[3][3]]]
		# # print(m)
		# m1=Matrix(m)
		# print(m1)
		# # r=1
		# # c=1
		# a,b=m1.jordan_form()
		# print(b)
		m=[[adj[1][1],adj[1][2],adj[1][3]],[adj[2][1],adj[2][2],adj[2][3]],[adj[3][1],adj[3][2],adj[3][3]]]
		
        # adjoint = threeBythree(cofactors,3)
		m1=Matrix(m)
		r=1
		c=1
		a,b=m1.jordan_form()
		# print(b)
		# for i in b:
		# 	print(i)
	
		# for x in range(1,4):
		# 	for y in range(1,4):
		# 		z = []

		# 		for i in range(1,4):
		# 			for j in range(1,4):
		# 				if (x==i) or (y==j):
		# 					pass
		# 				else:
		# 					z.append(B[i][j])
		# 		Z = [None,[None,z[0], z[1]], [None,z[2], z[3]]]
		# 		twoBytwoSub = twoBytwo(copy.deepcopy(Z),2)
		# 		subDeterminant = twoBytwoSub.determinant()
				
		# 		if ((x+y)%2 == 0):
		# 			coFactorElem = subDeterminant
		# 		else:
		# 			coFactorElem = -1 * subDeterminant

		# 		cofactors[x][y] = coFactorElem

		# cofactorsMatrix = threeBythree(cofactors,3)
		# adjoint = cofactorsMatrix.transpose()

		# for i in range(1,4):
		# 	for j in range(1,4):
		# 		adjoint.A[i][j] = round(adjoint.A[i][j]/float(mainDeterminant),3)
			# print(y)
		for i in b:
			print(i)
			if(r==1):
			    adj[1][1]=i
			if(r==2):
				adj[1][2]=i
			if(r==3):
				adj[1][3]=i
			if(r==4):
				adj[2][1]=i
			if(r==5):
				adj[2][2]=i
			if(r==6):
				adj[2][3]=i
			if(r==7):
				adj[3][1]=i
			if(r==8):
				adj[3][2]=i
			if(r==9):
				adj[3][3]=i
			r+=1
		print(adj)
		return threeBythree(adj,3)


if __name__ == '__main__': # the following code is only for testing purposes...this module is imported into app.py for its main use in the webapp.
	order = 2

	if order == 2:
		a11 = 1
		a12 = 2
		a21 = 3
		a22 = 4
		A = [None,[None,a11, a12], [None,a21, a22]]
		our_matrix = twoBytwo(copy.deepcopy(A),order) 
		x = our_matrix.inverse()
		print (x)

	if order == 3:
		a11 = 1
		a12 = 2
		a13 = 3
		a21 = 4
		a22 = 5
		a23 = 6
		a31 = 7
		a32 = 6
		a33 = 8
		A = [None,[None,a11, a12, a13], [None,a21, a22, a23], [None,a31, a32, a33]]
		matrixA = threeBythree(copy.deepcopy(A),order)
		x = matrixA.inverse()
		print( x)