type Customer = { id: string; description: string | null };
const customer: Customer = { id: 'cus_shiftproof_synthetic', description: null };
function label(value: Customer): string {
  return `${value.id}:${value.description ?? 'none'}`;
}
if (label(customer) !== 'cus_shiftproof_synthetic:none') throw new Error('unexpected label');
