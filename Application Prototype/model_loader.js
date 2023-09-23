import * as tf from '@tensorflow/tfjs';

async function loadModel() {
  try {
    //local directory
    const model = await tf.loadLayersModel('D:\Android Studio Project\Prototype1\ml_component\smishing_model.h5');
    return model;

  } catch (error) {
    console.error('Error loading the model:', error);
    throw error; // Optionally re-throw the error for error handling in your components
  }
}

export default loadModel;
