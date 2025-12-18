package Day_6;

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class trash_compactor {

    public static void main(String[] args) throws IOException {
        File file = new File("trash_compactor.txt");

        List<Boolean> used = new ArrayList<>();

        int totalLines = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                totalLines++;
                for (int i = 0; i < line.length(); i++) {
                    if (used.size() <= i) {
                        used.add(false);
                    }
                    if (line.charAt(i) != ' ') {
                        used.set(i, true);
                    }
                }
            }
        }


        List<int[]> problems = new ArrayList<>();
        int start = -1;

        for (int i = 0; i < used.size(); i++) {
            if (used.get(i)) {
                if (start == -1) start = i;
            } else {
                if (start != -1) {
                    problems.add(new int[]{start, i - 1});
                    start = -1;
                }
            }
        }
        if (start != -1) {
            problems.add(new int[]{start, used.size() - 1});
        }

        BigInteger grandTotal = BigInteger.ZERO;
        BigInteger grandTotal2 = BigInteger.ZERO;

        for (int[] p : problems) {
            BigInteger acc = BigInteger.ZERO;
            char operator;

            String lastLine = null;
            try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                String line;
                while ((line = br.readLine()) != null) {
                    lastLine = line;
                }
            }

            if (p[0] < lastLine.length()) {
                operator = lastLine
                        .substring(p[0], Math.min(p[1] + 1, lastLine.length()))
                        .trim()
                        .charAt(0);
            } else {
                continue;
            }

            acc = (operator == '*') ? BigInteger.ONE : BigInteger.ZERO;

            try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                String line;
                int row = 0;
                while ((line = br.readLine()) != null) {
                    row++;
                    if (row == totalLines) break;

                    if (p[0] >= line.length()) continue;
                    String token = line.substring(
                            p[0],
                            Math.min(p[1] + 1, line.length())
                    ).trim();

                    if (token.isEmpty()) continue;

                    BigInteger val = new BigInteger(token);
                    if (operator == '+') {
                        acc = acc.add(val);
                    } else {
                        acc = acc.multiply(val);
                    }
                }
            }

            grandTotal = grandTotal.add(acc);

            
            acc = (operator == '*') ? BigInteger.ONE : BigInteger.ZERO;

            for (int col = p[1]; col >= p[0]; col--) {

                BigInteger number = BigInteger.ZERO;

                try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                    String line;
                    int row = 0;

                    while ((line = br.readLine()) != null) {
                        row++;

                        if (row == totalLines) break;

                        if (col >= line.length()) continue;

                        char ch = line.charAt(col);
                        if (ch == ' ') continue;

                        int digit = ch - '0';
                        number = number.multiply(BigInteger.TEN)
                                    .add(BigInteger.valueOf(digit));
                    }
                }

                if (operator == '+') {
                    acc = acc.add(number);
                } else {
                    acc = acc.multiply(number);
                }
            }
            grandTotal2 = grandTotal2.add(acc);
        }

        System.out.println("Total: " + grandTotal);
        System.out.println("Total (reversed): " + grandTotal2);
    }
}
