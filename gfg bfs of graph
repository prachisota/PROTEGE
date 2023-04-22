class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        int s=0;
        vector<int>visit(V,0);
        vector<int>ans;
        queue<int>q;
        visit[s]=1;
        q.push(s);
        while(!q.empty())
        {
            int node=q.front();
            q.pop();
            ans.push_back(node);
            for(auto it:adj[node])
            {
                if(!visit[it])
                {visit[it]=1;
                q.push(it);}
            }
        }
        return ans;
    }
};
