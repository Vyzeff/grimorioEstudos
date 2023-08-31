import React from "react";
import { Text, Pressable } from "react-native";
import { styles } from "./styles";
interface RandomNumProps {
  id: string;
  number: number;
  isSelected: boolean;
  onPress: (index: string) => void;
}

export default function RandomNum({
  id,
  number,
  isSelected,
  onPress,
}: RandomNumProps) {
  const handleChoice = () => {
    onPress(id);
  };

  return (
    <Pressable onPress={handleChoice}>
      <Text style={[styles.randItem, isSelected && styles.selectedStyle]}>
        {number}
      </Text>
    </Pressable>
  );
}
