class Solution {
  public:
  void dfs(int s,vector<int>adj[],vector<int>&visit,vector<int>&ans)
  {
      visit[s]=1;
      ans.push_back(s);
      for(auto it:adj[s])
      {
          if(!visit[it])
          {
              dfs(it,adj,visit,ans);
          }
      }
  }
    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
    vector<int>visit(V,0);
        int s=0;
        vector<int>ans;
        dfs(s,adj,visit,ans);
        return ans;
        
    }
};
