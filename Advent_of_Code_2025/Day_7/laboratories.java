package Day_7;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class laboratories {

    static void dfs(char[][] grid, int x, int y, HashSet<List<Integer>> splPoints){
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length) {
            return;
        }

        char cell = grid[x][y];
        if (cell == '^') {
            splPoints.add(Arrays.asList(x, y));
            dfs(grid, x + 1, y - 1, splPoints);
            dfs(grid, x + 1, y + 1, splPoints);
        } else if (cell == '|') {
            return;
        } else {
            grid[x][y] = '|';
            dfs(grid, x + 1, y, splPoints);
        }
    }


    public static void main(String[] args)throws Exception {
        String content = Files.readString(Path.of("laboratories.txt"));
        int col = content.indexOf('\n');
        String[] lines = content.split("\n");
        int row = lines.length;
        char[][] grid = new char[row][col];
        for (int i = 0; i < row; i++) {
            grid[i] = lines[i].toCharArray();
        }
        
        char[][] gridCopy = new char[row][col];
        for (int i = 0; i < row; i++) {
            gridCopy[i] = Arrays.copyOf(grid[i], col);
        }
        HashSet<List<Integer>> splPoints = new HashSet<>();
        dfs(grid, 0, lines[0].indexOf('S'), splPoints);
        
        System.out.println("Number of beam splits: " + splPoints.size());

        long[][] ways = new long[row][col];
        ways[0][lines[0].indexOf('S')] = 1;

        for (int x = 0; x < row - 1; x++) {
            for (int y = 0; y < col; y++) {

                long k = ways[x][y];
                if (k == 0) continue;

                if (gridCopy[x][y] == '^') {
                    ways[x + 1][y - 1] += k;
                    ways[x + 1][y + 1] += k;
                } else {
                    ways[x + 1][y] += k;
                }
            }
        }

        long totalWays = 0;
        for (int y = 0; y < col; y++) {
            totalWays += ways[row - 1][y];
        }

        System.out.println("Total ways to reach the bottom: " + totalWays);
    }
}
