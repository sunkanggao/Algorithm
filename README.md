# Algorithm

## 链表队列栈

## 字符串

## 分治与递归

## 数组

## 树

## 图

[并查集计算图的联通分量个数](https://github.com/sunkanggao/Algorithm/blob/master/course/06_Graph/unionFindSet.py)

[并查集介绍](http://blog.csdn.net/dm_vincent/article/details/7655764)

[Floyd算法](https://github.com/sunkanggao/Algorithm/blob/master/course/06_Graph/floyd.py)

**计算割点**

1. 使用深度优先搜索，当前刚刚访问节点i，遍历节点i的相邻节点j；
2. 若j尚未访问，则如果不通过节点i，节点j直接连通的最早节点假定为k：如果节点k的访问顺序比i早，
说明节点j可以绕过节点i；如果节点k的访问顺序比i晚，说明想要访问节点j，必须经过节点i，即：节点i为割点。
3. 特殊处理根节点：若根节点的访问分支多于两个，则根节点为割点。

**判断某有向图是否为强连通图**

任取有向图G的某节点S，从S开始深度优先搜索，若可以遍历G的所有节点，则将G的所有边反向，再次从S开始进行
深度优先搜索，如果能够再次遍历G的所有节点，则G是强连通图，两次中有任何一次不满足则G不是强连通图。此外，
上述搜索可以换成广度优先搜索等其他方案。

**判断一个图是否有环**

 `拓扑排序`：从有向图中选择一个没有前驱的节点（即入度为0）并且输出它；从网中删去该节点，并删去由该节点发出的所有
有向边；重复上面两步，直到剩余的网中不再存在没有前驱的节点为止。若还有剩余的网，则说明原图有环。

 `并查集`

**最短路径问题**

`Dijkstra(迪杰斯特拉)算法`是典型的单源最短路径算法，用于计算一个节点到其他所有节点的最短路径。主要特点是以起始点为中心向外层层扩展，
直到扩展到终点为止。该算法要求图中不存在负权边。[详见此链接](http://www.cnblogs.com/biyeymyhjob/archive/2012/07/31/2615833.html)。

`Floyd-Warshall算法`又叫插点法，是解决任意两点间的最短路径的一种算法，可以正确处理有向图或负权的最短路径问题，
同时也被用于计算有向图的传递闭包。Floyd-Warshall算法的时间复杂度为O(N^3)，空间复杂度为O(N^2)。[详见此链接](http://www.cnblogs.com/biyeymyhjob/archive/2012/07/31/2615833.html)。

`A*算法（启发式搜索）`，给定有向图G，求从S到E的最短路径。从S到E的路径探索中，假定当前位于节点i，则与节点i相连的节点中，
应该选择哪个？定义f[j]:=g[j]+h[j]，g[j]为从起始节点S到节点j的距离，h[j]为从节点j到终止节点E的距离（该距离只要比真实距离小就行，比如直线距离）。
则应选择f[j]最小的节点作为i的后继。

`Bellman-ford算法`是单源点最短路径算法，对边权无要求，可以发现负环。动态规划算法，若u->v是有向边，
则d[v]<=d[u]+dis(u,v)。

**最小生成树MST**

`Prim算法`：贪心算法，从任意一个节点出发，选择与该节点邻接的权值最小的边，随着节点的不断加入，
每次都选择这些节点发出的边中权值最小的，重复n-1次。

`Kruskal算法`：贪心算法，将边按照权值递增排序，每次选择权值最小并且不构成环的边，重复n-1次。