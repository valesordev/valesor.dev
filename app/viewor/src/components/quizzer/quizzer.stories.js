import React from 'react';
import { action } from '@storybook/addon-actions';
import Quiz from './quizzer';

export default {
  title: 'Quiz',
  component: Quiz,
};

const question = 'What is the capital of France?';
const options = ['Paris', 'London', 'Berlin', 'Madrid'];

export const Default = () => (
  <Quiz question={question} options={options} selected={options[0]} onSubmit={action('Submit')} />
);

export const WithPreselectedOption = () => (
  <Quiz
    question={question}
    options={options}
    selected="London"
    onSubmit={action('Submit')}
  />
);
