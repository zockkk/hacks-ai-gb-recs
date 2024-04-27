export function TextArea() {
  return (
    <textarea
      id="message"
      rows={4}
      className="block p-2.5 w-full text-sm rounded-lg border bg-neutral-800 focus:ring-white focus:border-white"
      placeholder="Введите текст или ссылку на вакансию"
    />
  )
}