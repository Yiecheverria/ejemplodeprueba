import React from "react";
import {
  Image,
  Linking,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";
import { FontAwesome } from "@expo/vector-icons";
import { FontAwesome6 } from "@expo/vector-icons";

export default function PerfilScreen() {
  const urlPint = "https://www.pinterest.es/jesseniaechever/";
  const urlDiscord = "https://discord.com/channels/@me";
  const urlReddit = "https://www.reddit.com/";
  const urlSnap = "https://www.snapchat.com/";
  const urtele = "https://web.telegram.org/a/";

  return (
    <View style={styles.Container}>
      <View>
        <Text style={styles.text}>Mi Perfil</Text>
      </View>

      <View style={styles.img}>
        <Image
          source={require("../img/imagen.png")}
          style={{ width: 50, height: 50 }}
        />
        <Text  style = {{ margin: 20}}> Isabel Echeverria</Text>
      </View>

      <View>
        <Text style={styles.text}>Redes Sociales</Text>
      </View>

      <View style={styles.Icons}>
        {/** tipo boton para realizar una accion siempre a un componente */}
        <TouchableOpacity
          onPress={() => Linking.openURL(urlPint)}
          style={{ margin: 5 }}
        >
          <FontAwesome name="pinterest-square" size={60} color="red" />
          <Text>Pinterest</Text>
        </TouchableOpacity>

        {/** Discord*/}
        <TouchableOpacity
          onPress={() => Linking.openURL(urlDiscord)}
          style={{ margin: 5 }}
        >
          <FontAwesome6 name="discord" size={60} color="purple" />
          <Text>Discord</Text>
        </TouchableOpacity>

        {/** reddit*/}
        <TouchableOpacity
          onPress={() => Linking.openURL(urlReddit)}
          style={{ margin: 5 }}
        >
          <FontAwesome6 name="reddit" size={60} color="#FF5700" />
          <Text>Reddit</Text>
        </TouchableOpacity>

        {/** snapchat*/}
        <TouchableOpacity
          onPress={() => Linking.openURL(urlSnap)}
          style={{ margin: 5 }}
        >
          <FontAwesome name="snapchat-square" size={60} color="yellow" />
          <Text>Snapchat</Text>
        </TouchableOpacity>
        {/** telegram*/}
        <TouchableOpacity
          onPress={() => Linking.openURL(urtele)}
          style={{ margin: 5 }}
        >
          <FontAwesome name="telegram" size={60} color="blue" />
          <Text>Telegram</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
  Container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 20,
    fontWeight: "bold",
    marginTop: 40,
  },
  Icons: {
    flex: 1,
    margin: 20,
    flexDirection: "row",
  },
  img: {
    marginTop: 50,
    justifyContent : 'center',
    alignItems : "center",
  },
});
