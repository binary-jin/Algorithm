import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        List<Integer> list = new ArrayList<>();
        //ArrayList 사용해 중복 제거한 결과 저장
        
        list.add(arr[0]);
        //첫 번째 요소는 무조건 추가
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i-1]) {
                list.add(arr[i]);
            }
        }
        //배열을 순회하면서 연속된 중복 제거
        
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }


        return result;
    }
}