import React from 'react';
import { View, Text, Button } from 'react-native';

const MainPage = ({ navigation }) => {
  return (
    <View>
      <Text>Main Page</Text>
      <Button title="Menu" onPress={() => navigation.navigate('Menu')} />
    </View>
  );
};

export default MainPage;
