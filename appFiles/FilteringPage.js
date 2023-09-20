import React from 'react';
import { View, Text, Button } from 'react-native';

const FilteringPage = ({ navigation }) => {
  return (
    <View>
      <Text>Filtering Page</Text>
      {/* Add filtering options here */}
      <Button title="Go Back" onPress={() => navigation.goBack()} />
    </View>
  );
};

export default FilteringPage;
