import {Form} from "@/containers/Form/Form";

export default function Home() {
  return (
    <div className="w-full">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex"/>

      <div className="relative flex flex-col gap-12">
        <Form />
      </div>

      <div className="mb-32 grid text-center lg:mb-0 lg:w-full lg:max-w-5xl lg:grid-cols-4 lg:text-left"/>
    </div>
  );
}
