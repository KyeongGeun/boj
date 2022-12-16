import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genreScores = new HashMap<>();
        Map<Integer, Integer> songScores = new HashMap<>();
        Map<String, Integer> genreCount = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            songScores.put(i, play);
            if (!genreScores.containsKey(genre)) {
                genreScores.put(genre, 0);
                genreCount.put(genre, 0);
            }
            genreScores.replace(genre, genreScores.get(genre) + play);
        }

        ArrayList<Integer> list = new ArrayList<>();

        IntStream.range(0, genres.length)
                .boxed()
                .sorted(Comparator.comparing(i -> -genreScores.get(genres[(Integer) i]))
                        .thenComparing(i -> -songScores.get((Integer) i))
                        .thenComparing(i -> (Integer) i))
                .mapToInt(i -> i)
                .forEach(i -> {
                    String genre = genres[i];
                    if (genreCount.get(genre) < 2) {
                        genreCount.replace(genre, genreCount.get(genre) + 1);
                        list.add(i);
                    }
                });

        return list.stream().mapToInt(i -> i).toArray();
    }
}