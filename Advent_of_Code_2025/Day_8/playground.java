package Day_8;

import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

class Point{
    long x;
    long y;
    long z;

    double distance(Point other){
        return Math.sqrt(Math.pow(x - other.x, 2) + Math.pow(y - other.y, 2) + Math.pow(z - other.z, 2));
    }
}

class Edge{
    int pa; // point a index
    int pb; // point b index
    double weight; // distance between point a and point b
}

class DSU{
    private int[] parent;
    int[] size;
    
    public DSU(int n){
        parent = new int[n];
        size = new int[n];
        for(int i=0;i<n;i++){
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int i){
        if(parent[i] != i){
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }

    public void union(int a, int b){
        int rootA = find(a);
        int rootB = find(b);
        if(rootA == rootB) return;
        if(size[rootA] < size[rootB]){
            parent[rootA] = rootB;
            size[rootB] += size[rootA];
        } else {
            parent[rootB] = rootA;
            size[rootA] += size[rootB];
        }
    }

}

class DSU2{
    private int[] parent;
    int[] size;
    
    public DSU2(int n){
        parent = new int[n];
        size = new int[n];
        for(int i=0;i<n;i++){
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int i){
        if(parent[i] != i){
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }

    public int[] union(int a, int b, int n){
        int rootA = find(a);
        int rootB = find(b);
        if(rootA == rootB) return null;
        if(size[rootA] < size[rootB]){
            int temp = rootA;
            rootA = rootB;
            rootB = temp;
        }
        parent[rootB] = rootA;
        size[rootA] += size[rootB];
        // System.out.println(size[rootA]);
        if (size[rootA] == n) {
            return new int[]{a, b};
        }
        return null;
    }

}

public class playground {
    public static void main(String[] args)throws IOException{
        ArrayList<Point> points = new ArrayList<Point>();
        BufferedReader br = new BufferedReader(new FileReader("playground.txt"));
        String line;
        while((line=br.readLine())!=null){
            // 162,817,812
            String[] coords = line.split(",");
            Point p = new Point();
            p.x = Long.parseLong(coords[0]);
            p.y = Long.parseLong(coords[1]);
            p.z = Long.parseLong(coords[2]);
            points.add(p);
        }
        br.close();

        PriorityQueue<Edge> pq = new PriorityQueue<Edge>((a, b) -> Double.compare(b.weight, a.weight)); //max heap and max size is 1000
        
        for(int i=0;i<points.size();i++){
            for(int j=i+1;j<points.size();j++){
                Edge e = new Edge();
                e.pa = i;
                e.pb = j;
                e.weight = points.get(i).distance(points.get(j));
                if(pq.size() < 1000) {
                    pq.add(e);
                }
                else if(e.weight < pq.peek().weight){
                    pq.poll();
                    pq.add(e);
                }
            }
        }

        DSU dsu = new DSU(points.size());
        while(!pq.isEmpty()){
            Edge e = pq.poll();
            if(dsu.find(e.pa) != dsu.find(e.pb)){
                dsu.union(e.pa, e.pb);
            }
        }

        // Multiply top 3 largest size in the DSU object
        Arrays.sort(dsu.size);
        System.out.println(dsu.size[dsu.size.length - 1] * dsu.size[dsu.size.length - 2] * dsu.size[dsu.size.length - 3]);

        PriorityQueue<Edge> pq2 = new PriorityQueue<Edge>((a, b) -> Double.compare(a.weight, b.weight)); //min heap
        for(int i=0;i<points.size();i++){
            for(int j=i+1;j<points.size();j++){
                Edge e = new Edge();
                e.pa = i;
                e.pb = j;
                e.weight = points.get(i).distance(points.get(j));
                pq2.add(e);
            }
        }

        DSU2 dsu2 = new DSU2(points.size());
        while(!pq2.isEmpty()){
            Edge e = pq2.poll();
            int[] res = dsu2.union(e.pa, e.pb, points.size());
            if(res != null){
                System.out.println(points.get(res[0]).x * points.get(res[1]).x);
                break;
            }
        }

    }
}

