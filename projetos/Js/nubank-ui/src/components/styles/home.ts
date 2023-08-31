import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#820AD1",
  },
  content: {
    paddingHorizontal: 30,
  },
  header: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    width: "100%",
    paddingTop: 40,
  },
  card: {
    width: "100%",
    height: 190,
    backgroundColor: "#9500F6",
    borderRadius: 21,
    elevation: 3,
    marginBottom: 20,
    padding: 20,
    justifyContent: "space-between",
  },
  smallCard: {
    width: "100%",
    height: 120,
    backgroundColor: "#9500F6",
    borderRadius: 21,
    elevation: 5,
    padding: 20,
    justifyContent: "space-between",
  },
  smallCardHeader: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  smallCardHeaderText: {
    color: "#fff",
  },
  smallCardText: {
    color: "#fff",
    fontSize: 34,
    fontWeight: "600",
  },
  cardHeader: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  cardText: {
    color: "#fff",
    fontSize: 24,
    lineHeight: 36,
    fontWeight: "600",
  },
  footer: {
    paddingTop: 30,
    paddingLeft: 20,
  },
  footerText: {
    color: "#fff",
    marginHorizontal: 20,
    paddingBottom: 30,
    fontWeight: "600",
    fontSize: 14,
  },
  footerCard: {
    height: 127,
    width: 100,
    backgroundColor: "#9500F6",
    elevation: 5,
    borderRadius: 21,
    padding: 20,
    justifyContent: "space-between",
    marginLeft: 10,
  },
  footerCardText: {
    color: "#fff",
    fontWeight: "600",
    fontSize: 12,
    lineHeight: 18,
  },
  footerScroll: {
    height: 400,
  },
});
