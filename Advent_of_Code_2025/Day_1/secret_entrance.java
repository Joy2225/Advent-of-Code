package Day_1;

import java.io.*;
import java.util.*;

public class secret_entrance{
    public static void main(String args[]){ 
        int ans1 = 0;
        int ans2 = 0;
        int sum = 50;
        try{
            BufferedReader br = new BufferedReader(new FileReader("secret_entrance.txt"));
            String line;
            while((line = br.readLine()) != null){
                // System.out.println(line);
                char side = line.charAt(0);
                int number = Integer.parseInt(line.substring(1));
                int hit;
                
                if(side == 'R'){
                    hit = (100 - sum) % 100;
                    if (hit == 0 && number > 0) hit = 100;

                    if (hit <= number) {
                        ans2 += 1 + (number - hit) / 100;
                    }
                    sum = (sum + number) % 100;
                }
                else if(side == 'L'){
                    hit = sum % 100;
                    if (hit == 0 && number > 0) hit = 100;

                    if (hit <= number) {
                        ans2 += 1 + (number - hit) / 100;
                    }
                    sum = (sum - number%100 + 100) % 100;
                }
                if(sum == 0){
                    ans1 += 1;
                }
            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(ans1);
        System.out.println(ans2);
    }
}