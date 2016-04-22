import unittest

from sage.all import matrix, GF, QQ, Matrix, CDF, I, RDF
from abelfunctions.homology import (
    involution_matrix,

)

class HomologyTestData(unittest.TestCase):
    r"""Collection of tests cases from Kalla,Klein."""
    def setUp(self):
        atrott = Matrix(
            CDF,
            [[ 0.0000 + 0.0235*I, 0.0000 + 0.0138*I, 0.0000 + 0.0138*I],
             [ 0.0000 + 0.0000*I, 0.0000 + 0.0277*I, 0.0000 + 0.0000*I],
             [-0.0315 + 0.0000*I, 0.0000 + 0.0000*I, 0.0250 + 0.0000*I]])
        btrott = Matrix(
            CDF,
            [[-0.0315 + 0.0235*I, 0.0000 + 0.0138*I,-0.0250 + 0.0138*I],
             [ 0.0000 + 0.0000*I,-0.0250 + 0.0277*I, 0.0250 + 0.0000*I],
             [ 0.0000 - 0.0235*I, 0.0000 + 0.0138*I, 0.0000 + 0.0138*I]])

        # klein curve:
        aklein = Matrix(
            CDF,
            [[-0.9667 + 0.7709*I, 0.9667 + 0.2206*I, 0.9667 - 2.0073*I],
             [-1.2054 - 0.2751*I,-0.4302 + 0.8933*I,-1.7419 + 1.3891*I],
             [-0.4302 - 0.8933*I, 1.7419 + 1.3891*I,-1.2054 + 0.2751*I]])
        bklein = Matrix(
            CDF,
            [[-2.7085 - 0.6182*I,-0.2387 + 0.4958*I, 1.3969 - 1.1140*I],
             [-2.1721 - 1.7322*I, 0.5365 - 0.1224*I,-0.7753 - 1.6097*I],
             [ 0.9667 + 0.2206*I,-0.9667 + 2.0073*I,-0.9667 + 0.7709*I]])

        # fermat curve:
        afermat = Matrix(
            CDF,
            [[0.9270 + 0.0000*I, 0.0000 - 0.9270*I, 0.0000 - 0.9270*I],
             [0.0000 + 0.0000*I, 0.0000 + 0.0000*I, 0.0000 - 1.8541*I],
             [0.0000 + 0.9270*I,-0.9270 + 0.0000*I, 0.0000 - 0.9270*I]])
        bfermat = Matrix(
            CDF,
            [[0.9270 + 0.9270*I, 0.9270 - 0.9270*I, 0.0000 + 0.0000*I],
             [0.0000 + 0.0000*I,-0.9270 + 0.9270*I, 0.9270 - 0.9270*I],
             [-0.9270+ 0.0000*I, 0.0000 - 0.9270*I, 0.0000 - 0.9270*I]])

        # a genus six curve
        a6 = Matrix(
            CDF,
            [
                [0.041441136367794 + 0.027833200726691*I, -0.034538213432710 + 0.027188711893010*I, -0.097853547524326 + 0.026426118256733*I, -0.304059718474855 + 0.060306772513671*I, -0.536899366726663 + 0.087203183867874*I, -2.814882797646379 + 0.543317148745872*I],
                [-0.114912806296197 - 0.044601420984340*I, 0.000000000000002 - 0.000000000000002*I, 0.053195632592273 - 0.022598899319034*I, 0.000000000000006 - 0.000000000000006*I, 0.242671354734388 + 0.009863612111086*I, 0.764112818309978 + 0.035735030643330*I],
                [0.114912806296198 + 0.016851233729331*I, -0.000000000000003 + 0.054377423786101*I, -0.053195632592272 - 0.080539669725953*I, -0.000000000000009 + 0.120613545027839*I, -0.242671354734385 - 0.237235882811205*I, -0.764112818309973 - 0.538148249906231*I],
                [-0.000000000000145 - 0.011064980468868*I, -0.000000000000232 + 0.018296506388701*I, -0.000000000000371 - 0.030253337193984*I, -0.000000000001418 + 0.111441672814486*I, -0.000000000002271 - 0.184269979844065*I, -0.000000000013900 - 1.122369328118062*I],
                [0.081988303080824 - 0.027750187255008*I, -0.000000000000001 - 0.000000000000000*I, -0.052735643727852 - 0.103138569044988*I, -0.000000000000002 - 0.000000000000001*I, -0.088120274254757 - 0.227372270700121*I, -0.127496577243115 - 0.502413219262904*I],
                [-0.081988303080827 + 0.000000000000001*I, -0.000000000000003 - 0.054377423786097*I, 0.052735643727848 + 0.0000000000000058*I, -0.000000000000006 - 0.120613545027826*I, 0.088120274254749 + 0.000000000000010*I, 0.127496577243099 + 0.000000000000019*I],
            ]
        )
        b6 = Matrix(
            CDF,
            [
                [0.041441136367794 + 0.027833200726690*I, -0.034538213432710 - 0.009404300883654*I, -0.097853547524326 + 0.026426118256743*I, -0.304059718474855 - 0.162576573110822*I, -0.536899366726663 + 0.087203183867912*I, -2.814882797646379 + 0.543317148746025*I],
                [-0.008893776107028 - 0.100911791871047*I, -0.066617940934943 + 0.018040458698884*I, 0.109123013300482 - 0.073253290304226*I, -0.116239263979475 + 0.004585936107792*I, 0.338049660213882 - 0.105519234924677*I, 0.955517317106568 - 0.261883524016635*I],
                [-0.008893776107028 - 0.056310370886708*I, -0.066617940934943 - 0.018040458698885*I, 0.109123013300482 - 0.050654390985187*I, -0.116239263979475 - 0.004585936107801*I, 0.338049660213882 - 0.115382847035744*I, 0.955517317106568 - 0.297618554659892*I],
                [0.032030533560343 - 0.000000000000020*I, 0.000000000000434 - 0.018296506388225*I, 0.142511462455675 - 0.000000000000020*I, 0.000000000002647 - 0.111441672811588*I, 0.831127378714640 - 0.000000000000147*I, 4.865652776956537 - 0.000000000001017*I],
                [0.106019030189168 + 0.028560183631701*I, 0.066617940934943 + 0.072417882484992*I, 0.055927380708208 - 0.052484178059800*I, 0.116239263979479 + 0.125199481135651*I, 0.095378305479493 - 0.111989423664385*I, 0.191404498796592 - 0.204794664603068*I],
                [-0.057957575972479 + 0.016041237352642*I, 0.066617940934944 - 0.036336965087211*I, 0.161398668163915 + 0.075083077378845*I, 0.116239263979481 - 0.116027608920027*I, 0.271618853989010 + 0.102125811553314*I, 0.446397653282827 + 0.169059633959730*I],
            ]
        )

        # store matrices
        self.atrott = atrott
        self.btrott = btrott
        self.aklein = aklein
        self.bklein = bklein
        self.afermat = afermat
        self.bfermat = bfermat
        self.a6 = a6
        self.b6 = b6

        # klein curve
        Hklein = matrix(GF(2),[
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ])
        Qklein = matrix(GF(2),[
            [1,1,1],
            [0,0,1],
            [0,1,0],
        ])

        # fermat curve n=4 (g=3)
        Hfermat4 = matrix(GF(2),[
            [0,1,0],
            [1,0,0],
            [0,0,0]
        ])
        Qfermat4 = matrix(GF(2),[
            [1,0,0],
            [0,0,1],
            [0,1,0],
        ])

        # fermat curve n=5 (g=6)
        Hfermat5 = matrix(GF(2),[
            [1,0,0,0,0,0],
            [0,1,0,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,1,0],
            [0,0,0,0,0,1],
        ])
        Qfermat5 = matrix(GF(2),[
            [1,0,0,0,0,0],
            [1,0,0,1,0,0],
            [0,0,0,0,1,0],
            [0,0,1,0,1,0],
            [0,1,1,0,1,0],
            [0,0,1,0,1,1],
        ])

        # a genus 3 curve similar to f2
        Hf2a = matrix(GF(2),[
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ])
        Qf2a = matrix(GF(2),[
            [1,1,1],
            [0,0,1],
            [0,1,0],
        ])

        # a genus 6 curve
        H6 = matrix(GF(2),[
            [0,1,0,0,0,0],
            [1,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
        ])
        Q6 = matrix(GF(2),[
            [1,0,0,0,0,0],
            [0,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,1,0,0,1,0],
            [0,0,0,1,0,0],
            [0,0,0,0,1,1],
        ])

        # store
        self.Hklein = Hklein
        self.Qklein = Qklein
        self.N1klein = Qklein*Hklein*Qklein.T

        self.Hfermat4 = Hfermat4
        self.Qfermat4 = Qfermat4
        self.N1fermat4 = Qfermat4*Hfermat4*Qfermat4.T

        self.Hfermat5 = Hfermat5
        self.Qfermat5 = Qfermat5
        self.N1fermat5 = Qfermat5*Hfermat5*Qfermat5.T

        self.Hf2a = Hf2a
        self.Qf2a = Qf2a
        self.N1f2a = Qf2a*Hf2a*Qf2a.T

        self.H6 = H6
        self.Q6 = Q6
        self.N16 = Q6*H6*Q6.T


class TestInvolutionMatrix(HomologyTestData):
    def test_integral(self):
        # the integrality test is built into the function itself since the
        # return type should be a matrix over ZZ
        R = involution_matrix(self.atrott, self.btrott)
        R = involution_matrix(self.aklein, self.bklein, tol=1e-3)
        R = involution_matrix(self.afermat, self.bfermat, tol=1e-3)
        R = involution_matrix(self.a6, self.b6)

    def test_eigenvalues(self):
        R = involution_matrix(self.atrott, self.btrott)
        evals = R.eigenvalues()
        self.assertSetEqual(set(evals), {1.0, -1.0})

        R = involution_matrix(self.aklein, self.bklein, tol=1e-3)
        evals = R.eigenvalues()
        self.assertSetEqual(set(evals), {1.0, -1.0})

        R = involution_matrix(self.afermat, self.bfermat, tol=1e-3)
        evals = R.eigenvalues()
        self.assertSetEqual(set(evals), {1.0, -1.0})

        R = involution_matrix(self.a6, self.b6)
        evals = R.eigenvalues()
        self.assertSetEqual(set(evals), {1.0, -1.0})

    def test_diagonalizable(self):
        R = involution_matrix(self.atrott, self.btrott)
        RQQ = R.change_ring(QQ)
        self.assertTrue(RQQ.is_diagonalizable())

        R = involution_matrix(self.aklein, self.bklein, tol=1e-3)
        RQQ = R.change_ring(QQ)
        self.assertTrue(RQQ.is_diagonalizable())

        R = involution_matrix(self.afermat, self.bfermat, tol=1e-3)
        RQQ = R.change_ring(QQ)
        self.assertTrue(RQQ.is_diagonalizable())

        R = involution_matrix(self.a6, self.b6)
        RQQ = R.change_ring(QQ)
        self.assertTrue(RQQ.is_diagonalizable())


# class TestSymmetricFactorization(unittest.TestCase):
#     def setUp(self):

#     def test_rank(self):
#         H,Q = None, None
#         assert(H.rank() == N1.rank())
#         assert(norm(H - H.T) == 0)
#         assert(Q*H*Q.T == N1)

