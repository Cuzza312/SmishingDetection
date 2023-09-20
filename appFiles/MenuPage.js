import React from 'react';
import { View, Text, Button } from 'react-native';

const MenuPage = ({ navigation }) => {
  return (
    <View>
      <Text>Menu Page</Text>
      <Button title="Messages" onPress={() => navigation.navigate('Main')} />
      <Button title="Filtering Rules" onPress={() => navigation.navigate('FilteringRules')} />
      <Button title="Settings" onPress={() => navigation.navigate('Settings')} />
      <Button title="Account" onPress={() => navigation.navigate('Account')} />
      <Button title="Feedback" onPress={() => navigation.navigate('Feedback')} />
    </View>
  );
};

export default MenuPage;
