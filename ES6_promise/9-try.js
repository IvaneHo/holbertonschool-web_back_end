export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const value = mathFunction();
    queue.push(value);
  } catch (err) {
    queue.push(err.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
