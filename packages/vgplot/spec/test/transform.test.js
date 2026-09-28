import { expect, it } from 'vitest';
import { abs, avg, div, isAggregateExpression, round, sql, sum } from '@uwdata/mosaic-sql';
import * as vg from '@uwdata/vgplot';
import { parseSpec } from '../src/index.js';

it('instantiates nested transforms and SQL expressions', () => {
  const ast = parseSpec({
    plot: [{
      mark: 'lineY',
      data: { from: 'sales' },
      x: 'day',
      y: { sum: { sum: { sql: 'amount' } }, orderby: 'day' },
    }],
  });
  const actual = ast.root.children[0].options.instantiate({ api: { sql, sum } }).y;
  expect(isAggregateExpression(actual)).toBe(1);
  expect(String(actual)).toBe(String(sum(sum(sql`amount`)).orderby('day')));
});

it('instantiates numeric transforms over aggregates', () => {
  const ast = parseSpec({
    plot: [{
      mark: 'barX',
      data: { from: 't' },
      x: { abs: { sum: { sql: 'a' } } },
      y: { round: [{ avg: 'a' }, 2] },
    }],
  });
  const { x, y } = ast.root.children[0].options.instantiate({ api: { abs, avg, round, sql, sum } });
  expect(isAggregateExpression(x)).toBe(1);
  expect(String(x)).toBe(String(abs(sum(sql`a`))));
  expect(isAggregateExpression(y)).toBe(1);
  expect(String(y)).toBe(String(round(avg('a'), 2)));
});

it('instantiates arithmetic transforms with the vgplot API', () => {
  const ast = parseSpec({
    plot: [{
      mark: 'barY',
      data: { from: 't' },
      x: 'c',
      y: { div: [{ sum: 'a' }, { sum: 'b' }] },
    }],
  });
  const { y } = ast.root.children[0].options.instantiate({ api: vg });
  expect(isAggregateExpression(y)).toBe(1);
  expect(String(y)).toBe(String(div(sum('a'), sum('b'))));
});
