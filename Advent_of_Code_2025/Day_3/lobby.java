package Day_3;

import java.io.*;

import java.util.Stack;
public class lobby {
    public static void main(String[] args)throws IOException {
        int sum = 0;
        long sum12 = 0;
        try{
            BufferedReader r = new BufferedReader(new FileReader("lobby.txt"));
            String line;
            while((line = r.readLine()) != null){

                sum += getreqnumber_size_2(line);
                System.out.println(getreqnumber_size_12(line));
                sum12 += getreqnumber_size_12(line);
            }

        }catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(sum);
        System.out.println(sum12);
    }

    public static int getreqnumber_size_2(String line){
        int largest = -1;
        int secondlargest = -1;
        for(int i = 0; i < line.length(); i++){
            int currentdigit = Character.getNumericValue(line.charAt(i));
            if(i==line.length()-1){
                if(currentdigit > secondlargest){
                    secondlargest = currentdigit;
                }
            }else{
                if(currentdigit > largest){
                    secondlargest = -1;
                    largest = currentdigit;
                }else if(currentdigit > secondlargest){
                    secondlargest = currentdigit;
                }
            }
        }
        return largest * 10 + secondlargest;        
        
    }

    public static long getreqnumber_size_12(String line){
        
        Stack<Integer> stack = new Stack<>();
        int k = 12;
        int r = line.length() - k;
        for(int i = 0; i < line.length(); i++){
            int currentdigit = line.charAt(i) - '0';
            while(!stack.isEmpty() && r > 0 && stack.peek() < currentdigit){
                stack.pop();
                r--;
            }
            stack.push(currentdigit);

            
        }
        while(stack.size()>k){
            stack.pop();
        }

        long reqnumber = 0;
        for(int digit : stack){
            reqnumber = reqnumber * 10 + digit;
        }
        return reqnumber;
    }
}
