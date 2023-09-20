import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import MainPage from './MainPage';
import MenuPage from './MenuPage';
import FilteringPage from './FilteringPage';
import SettingsPage from './SettingsPage';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Main">
        <Stack.Screen name="Main" component={MainPage} />
        <Stack.Screen name="Menu" component={MenuPage} />
        <Stack.Screen name="FilteringRules" component={FilteringPage} />
        <Stack.Screen name="Settings" component={SettingsPage} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
