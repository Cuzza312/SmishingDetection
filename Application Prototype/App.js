import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const App = () => {
  const [text, setText] = useState('');
  const [displayText, setDisplayText] = useState('');

  const handleButtonClick = () => {
    setDisplayText(text);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Enter Text:</Text>
      <TextInput
        style={styles.input}
        placeholder="Type something..."
        onChangeText={(newText) => setText(newText)}
        value={text}
      />
      <Button
        title="Submit"
        onPress={handleButtonClick}
        style={styles.button}
      />
      <Text style={styles.displayText}>You entered: {displayText}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  label: {
    fontSize: 18,
    marginBottom: 10,
  },
  input: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 10,
    marginBottom: 20,
  },
  button: {
    width: '60%',
  },
  displayText: {
    fontSize: 16,
    marginTop: 20,
  },
});

export default App;
