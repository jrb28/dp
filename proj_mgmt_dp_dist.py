# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:23:09 2017

@author: jrbrad
"""

dist = {}

def f_star(net,state,dest):
    if state == dest:
        dist[state] = 0
        return dist[state]
    elif state in net.keys():
        alts = []
        for (key,cost) in net[state]:
            f_star_cost = f_star(net,key,dest)
            alts.append(cost + f_star_cost)
        dist[state] = max(alts)
        return dist[state]

if __name__ == "__main__":
    """ shortest path Wmsbg to LA """
    links = {'A':[('B', 10)], 'B':[('C', 3), ('D', 3)], 'C':[('E', 1)], 'D':[('E',6), ('F',6), ('G',6)], 'E':[('FINISH', 4)], 'F':[('H', 3)], 'G':[('H', 5)], 'H':[('FINISH', 1)]}
    origin = 'A'
    dest = 'FINISH'

    f_star(links,origin,dest)
    
    print(f'Total Elapsed Time: {dist[origin] }\n')
    
    for loc in dist.keys():
        print(loc,":",dist[loc])