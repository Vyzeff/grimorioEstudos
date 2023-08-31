import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#ddd",
  },
  target: {
    margin: 50,
    color: "red",
    fontSize: 50,
    backgroundColor: "#aaa",
    textAlign: "center",
  },
  randContainer: {
    flex: 1,
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "space-around",
  },
  randItem: {
    fontSize: 30,
    backgroundColor: "#bbb",
    width: 100,
    marginHorizontal: 15,
    marginVertical: 25,
    textAlign: "center",
  },
  selectedStyle: {
    opacity: 0.3,
  },
});
