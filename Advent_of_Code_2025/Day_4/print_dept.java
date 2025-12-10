package Day_4;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;

public class print_dept {
    public static void main(String[] args) throws IOException {
        String content = Files.readString(Path.of("print_dept.txt"));
        int row = content.indexOf('\n');
        int col = content.indexOf('\n');
        int matrix[][] = new int[row][col];
        int res = 0;
        String[] lines = content.split("\n");
        for(int r = 0; r < lines.length; r++){
            String line = lines[r];
            for(int i = 0; i < line.length(); i++){
                matrix[r][i] = line.charAt(i) == '@' ? 1 : 0;
            }
        }

        // for(int i=0; i<row; i++){
        //     for(int j=0; j<col; j++){
        //         System.out.print(matrix[i][j]);
        //     }
        //     System.out.println();
        // }

        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                // Adjacent 8 cells max should have 3 @
                int count = 0;
                if(matrix[i][j] == 0) continue;
                for(int x = -1; x <= 1; x++){
                    for(int y = -1; y <= 1; y++){
                        if(x == 0 && y == 0) continue;
                        int ni = i + x, nj = j + y;
                        if(ni >= 0 && ni < row && nj >= 0 && nj < col && matrix[ni][nj] == 1){
                            count++;
                        }
                    }
                }
                if(count <= 3) {
                    // System.out.println(i+" "+j);
                    res++;
                }
            }
        }
        System.out.println(res);

        int res2 = 0;
        int c=-1;
        while (c<res2){
            c = res2;
            for(int i = 0; i < row; i++){
                for(int j = 0; j < col; j++){
                    // Adjacent 8 cells max should have 3 @
                    int count = 0;
                    if(matrix[i][j] == 0) continue;
                    for(int x = -1; x <= 1; x++){
                        for(int y = -1; y <= 1; y++){
                            if(x == 0 && y == 0) continue;
                            int ni = i + x, nj = j + y;
                            if(ni >= 0 && ni < row && nj >= 0 && nj < col && matrix[ni][nj] == 1){
                                count++;
                            }
                        }
                    }
                    if(count <= 3) {
                        // System.out.println(i+" "+j);
                        matrix[i][j] = 0;
                        res2++;
                    }
                }
            }
            // System.out.println(res2);
        }
        System.out.println(res2);
    }
}
