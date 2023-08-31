import { StyleSheet } from "react-native";

import EditScreenInfo from "../../components/EditScreenInfo";
import { Text, View } from "../../components/Themed";
import { SafeAreaView } from "react-native-safe-area-context";
import { ScrollView } from "react-native-gesture-handler";
import LottieView from "lottie-react-native";
import threadsAnim from "../../assets/lottie-animations/threadsLogo.json";

export default function TabOneScreen() {
  return (
    <SafeAreaView>
      <ScrollView>
        <LottieView
          source={threadsAnim}
          loop={true}
          autoPlay={true}
          style={{ width: 90, height: 90, alignSelf: "center" }}
        />
      </ScrollView>
    </SafeAreaView>
  );
}
