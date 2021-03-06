let answer = 0

const nums = cents => {
  if (cents > 24) {
    const q = quatersFunc(cents)
    const t = tensFunc(q)
    const f = fivesFunc(t)
    const o = onesFunc(f)
  }
  if (cents > 9 && cents < 25) {
    const t = tensFunc(cents)
    const f = fivesFunc(t)
    const o = onesFunc(f)
  }
  if (cents > 4 && cents < 10) {
    const f = fivesFunc(cents)
    const o = onesFunc(f)
  }
  if (cents >= 0 && cents < 5) {
    return cents
  }
  return answer
}

const onesFunc = cents => {
  const ones = cents % 1
  answer += Math.floor(cents / 1)
  return ones
}

const fivesFunc = cents => {
  const fives = cents % 5
  answer += Math.floor(cents / 5)
  return fives
}

const tensFunc = cents => {
  const tens = cents % 10
  answer += Math.floor(cents / 10)
  return tens
}

const quatersFunc = cents => {
  const quaters = cents % 25
  answer += Math.floor(cents / 25)
  return quaters
}
