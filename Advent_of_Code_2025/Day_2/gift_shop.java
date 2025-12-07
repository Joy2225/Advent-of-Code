package Day_2;

import java.io.*;

public class gift_shop{
    public static void main(String args[]){ 
        long sum = 0;
        try{
            BufferedReader br = new BufferedReader(new FileReader("gift_shop.txt"));
            int ch;
            String id_range = "";
            while((ch = br.read()) != -1){
                char c = (char) ch;
                if (c==','){
                    // System.out.println(id_range);
                    sum += invalidSum(id_range);
                    id_range = "";
                } else {
                    id_range += c;
                }
            }
            System.out.println(id_range);
            sum += invalidSum(id_range);
            System.out.println(sum);
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static long invalidSum(String id_range){
        long sum = 0;
        id_range = id_range.trim();
        String[] parts = id_range.split("-");
        long start = Long.parseLong(parts[0]);
        long end = Long.parseLong(parts[1]);
        for (long i = start; i <= end; i++){
            String id = Long.toString(i);
            String temp = id.substring(1)+id.substring(0,id.length()-1);
            if (temp.contains(id)){
                System.out.println("Found repeating ID: " + id);
                System.out.println(temp);
                sum += i;
            }
        }

        return sum;
    }
}