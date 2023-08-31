import { Image, Text, View, ScrollView } from "react-native";
import { styles } from "../styles/home";
import logoImg from "../../../assets/logo.png";
import settingImg from "../../../assets/setting.png";
import masterImg from "../../../assets/mastercard.png";
import folderImg from "../../../assets/Wallet.png";
import pixImg from "../../../assets/pix.png";
import boletoImg from "../../../assets/boleto.png";
import dinheiroImg from "../../../assets/dinheiro.png";

export function Home() {
  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <View style={styles.header}>
          <Image source={logoImg} />
          <Image source={settingImg} />
        </View>
        <View style={styles.card}>
          <View style={styles.cardHeader}>
            <View />
            <Image source={masterImg} />
          </View>
          <View>
            <Text style={styles.cardText}>Alga</Text>
          </View>
        </View>
        <View style={styles.smallCard}>
          <View style={styles.smallCardHeader}>
            <Text style={styles.smallCardHeaderText}>Saldo Disponível</Text>
            <Image source={folderImg} />
          </View>
          <View>
            <Text style={styles.smallCardText}>R$234,14</Text>
          </View>
        </View>
      </View>
      <View style={styles.footer}>
        <Text style={styles.footerText}>Do que precisa?</Text>
        <ScrollView
          style={styles.footerScroll}
          showsHorizontalScrollIndicator={false}
          horizontal={true}
        >
          <View style={styles.footerCard}>
            <Image source={pixImg} />
            <Text style={styles.footerCardText}>Fazer um pix</Text>
          </View>
          <View style={styles.footerCard}>
            <Image source={dinheiroImg} />
            <Text style={styles.footerCardText}>Receber dinheiro</Text>
          </View>
          <View style={styles.footerCard}>
            <Image source={boletoImg} />
            <Text style={styles.footerCardText}>Pagar boleto</Text>
          </View>
        </ScrollView>
      </View>
    </View>
  );
}
