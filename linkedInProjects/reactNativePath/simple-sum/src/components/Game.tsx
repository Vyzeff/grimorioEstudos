import { Text, View } from "react-native";
import { useState } from "react";
import { styles } from "./styles";
import RandomNum from "./RandomNum";

interface GameProps {
  randChoiceNum: number;
}

export default function Game({ randChoiceNum }: GameProps) {
  const randChoices = Array.from({ length: randChoiceNum }).map(
    () => 1 + Math.floor(10 * Math.random())
  );

  const target = randChoices
    .slice(0, randChoiceNum - 2)
    .reduce((acc, curr) => acc + curr, 0);

  let [selectedNums, setSelectedNums] = useState("");

  const isSelected = (numberIndex: number) => {
    return selectedNums.indexOf("" + numberIndex) >= 0;
  };

  return (
    <View style={styles.container}>
      <Text style={styles.target}>{target}</Text>
      <View style={styles.randContainer}>
        {randChoices.map((randNum, index) => (
          //
          <RandomNum
            id={"" + index}
            key={index}
            number={randNum}
            isSelected={isSelected(index)}
            onPress={setSelectedNums}
          />
        ))}
      </View>
    </View>
  );
}
