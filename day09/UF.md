# UF



### 1. Parent == 부모리스트 생성

```python
parent = list(range(n+1))
```



### 2. Find 함수 생성

- 기본 로직

  ```python
  def find(x):
      if parent[x] == x:
          return x
      else:
          return find(parent[x])
  ```



- Path compression

  ```python
  def find(x):
      if parent[x] == x:
          return
      else:
          parent[x] = find(parent[x])
          return parent[x]
  ```

  





### 3. Union 함수 생성

- 기본 로직

  ```python
  def union(x, y):
      a = find(x)
      b = find(y)
      parent[b] = a
  ```



- Union by rank

  ```python
  rank = [0] * (n+1)
  
  def union(x, y):
      a = find(x)
      b = find(y)
      
      # 랭크가 더 큰 쪽 밑에 작은 부분을 합쳐서 최대한 간결하게 만드는것!
      if rank[a] < rank[b]:
          parent[a] = b
      elif rank[a] > rank[b]:
          parent[b] = a
      else:
          parent[a] = b
          rank[b] += 1
  ```

  







