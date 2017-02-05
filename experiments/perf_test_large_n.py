from __future__ import division
import fusion_prod.cbd as cbd
import cProfile, time

#Tests the performance of rank and divisor calculations for r=4, l=4, n=9, weight=[0,1,1,0]
#and small weights.
#Original time: 63 seconds
#After flattening IrrRep: 53 seconds
#After making Weight a subclass of tuple: 64 sec
#After adding fte_dict: 41 sec
#Unsafely optimizing get_rep_dim: 23 sec
#Removing Weight class: 10.5 sec
def experiment():
    rank = 4
    level = 4
    num_points = 9

    liealg = cbd.TypeALieAlgebra(rank, store_fusion=True)
    V = cbd.SymmetricConformalBlocksBundle(liealg, [0,1,1,0], num_points, level)
    print(V.getRank())

if __name__ == '__main__':
    t0 = time.clock()
    experiment()
    print(time.clock() -t0)
    #cProfile.run('experiment()', sort='cumtime')