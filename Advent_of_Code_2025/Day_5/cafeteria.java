package Day_5;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

class Interval{
    long start;
    long end;
    Interval(long s, long e){
        this.start = s;
        this.end = e;
    }
}

class Node{
    Interval i;
    long max;
    Node left, right;
}

class cafeteria {
    static Node newNode(Interval i) {
        Node temp = new Node();
        temp.i = i;
        temp.max = i.end;
        temp.left = null;
        temp.right = null;
        return temp;
    }

    static Node insert(Node root, Interval i){
        if(root == null){
            return newNode(i);
        }

        long key = root.i.start;

        if(i.start < key){
            root.left = insert(root.left, i);
        } else {
            root.right = insert(root.right, i);
        }

        if(root.max < i.end){
            root.max = i.end;
        }

        return root;
    }

    static void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.println("[" + root.i.start + ", " + root.i.end + "]" + " max = " + root.max);
        inorder(root.right);
    }

    static boolean findFresh(Node root, long val){
        if(root == null) return false;
        if(val > root.max) return false;

        if(root.i.start <= val && val <= root.i.end){
            return true;
        }

        return findFresh(root.left, val) || findFresh(root.right, val);
    }

    static ArrayList<long[]> mergeIntervals(String[] intervals) {
        ArrayList<long[]> merged = new ArrayList<>();
        ArrayList<long[]> intervalList = new ArrayList<>();
        for(String interval : intervals){
            String[] parts = interval.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);
            intervalList.add(new long[]{start, end});
        }

        // Sort intervals based on start time
        intervalList.sort((a, b) -> Long.compare(a[0], b[0]));

        long[] current = intervalList.get(0);
        for(int i = 1; i < intervalList.size(); i++){
            long[] next = intervalList.get(i);
            if(current[1] >= next[0]){
                current[1] = Math.max(current[1], next[1]);
            } else {
                merged.add(current);
                current = next;
            }
        }
        merged.add(current);
        return merged;
    }

    public static void main(String[] args) throws IOException {
        String content = Files.readString(Path.of("cafeteria.txt"));
        String[] lines = content.split("\n\n");

        String[] intervals = lines[0].split("\n");
        String[] requests = lines[1].split("\n");

        Node root = null;

        for(String interval : intervals){
            String[] parts = interval.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);
            root = insert(root, new Interval(start, end));
        }
        // inorder(root);
        long sum = 0;
        
        for(String request : requests){
            long val = Long.parseLong(request);
            if(findFresh(root, val)){
                sum ++;
            }
        }

        System.out.println(sum);        

        // Remove overlapping intervals and merge them
        ArrayList<long[]> mergedIntervals = mergeIntervals(intervals);
        long mergedSum = 0;
        for(long[] interval : mergedIntervals){
            mergedSum += (interval[1] - interval[0] + 1);
        }
        System.out.println(mergedSum);
    }
}