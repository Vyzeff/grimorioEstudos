import { View } from "react-native";
import Home from "./src/components/Home";
import { styles } from "./src/components/styles";

export default function App() {
  return (
    <View style={styles.container}>
      <Home />
    </View>
  );
}
